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
| **POTENTIAL** (K4 V-sector) | total TLM link-pulse energy, assigned to the potential register (**ENGINEERING-CHOICE**: ½ capacitive + ½ inductive — a traveling link pulse carries equal E/B energy; not "node capacitor charge") | `Σ_port (V_inc² + V_ref²)` per site | [`k4_tlm.py:528-530`](../src/ave/core/k4_tlm.py) `get_energy_density()` | per-port pulses summed to the **home node** |
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
> The **POTENTIAL** register (displacement / charge storage) =
> `k4.get_energy_density()` (K4 V-sector total link-pulse energy `Σ_port V_inc²+V_ref²`,
> `k4_tlm.py:528-530` — **ENGINEERING-CHOICE**: the whole TLM link-pulse energy is assigned to the
> potential register even though a traveling link pulse is ½ capacitive + ½ inductive in the TLM
> formalism [`V²=½(V_inc+V_ref)²+½(V_inc−V_ref)²`, and `Phi_link` accumulates from the same pulses,
> `k4_tlm.py:400`]; K4 energy is ~1.4e-3 of H and is included **identically** in both instruments,
> so this label choice moves no bin) +
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

## 5 · Sponge exclusion — the honest result (phase-robust)

**No — and the honest "why not" is *stronger* than the register-discriminator the earlier draft
claimed.** The frozen §5 argument ("the potential register is the boundary-clean one; the
CONCENTRATING is kinetic-specific") rested entirely on the drive-off → final-step **endpoint**,
and on the PML box the endpoint is a single LC-slosh **phase moment** (review MAJOR 1). Under the
phase-robust **quiet-window mean** the discriminator collapses and the honest picture is simpler
and firmer.

**(1) Time-averaged, NEITHER register is boundary-insensitive on the PML box.** Quiet-window-mean
`CF_peak_2.0`, frozen disjunctive rule, PML `pair` (guard sweep; `energy_pot` / `energy_pot_g1` /
`energy_pot_g2` and `energy_full_g0` / `energy_full` / `energy_full_g2`):

| PML pair, quiet-window mean | guard 0 | guard 1 (shipped) | guard 2 |
|---|---|---|---|
| POTENTIAL (`energy_pot`) peak-CF | +0.107 | +0.528 | +0.914 |
| POTENTIAL signature | CONCENTRATING | CONCENTRATING | CONCENTRATING |
| FULL (`energy_full`) peak-CF | +0.329 | +0.977 | +0.892 |
| FULL signature | CONCENTRATING | CONCENTRATING | CONCENTRATING |

The endpoint pot series the earlier draft called "boundary-clean LOOP-FILLING" (−0.364 / −0.311 /
−0.128) actually climbs monotonically toward CONCENTRATING with guard — the **same** direction as
the full/kinetic series, not the opposite — and its final-step value is a phase minimum
(`_nonmonotone_flag` fires on `CF_peak_2.0`). Time-averaged it reads CONCENTRATING at every guard.
So the potential register **CONCENTRATES on the PML box (quiet-mean) while it is LOOP-FILLING on
the torus**; the full register likewise. **The PML twins provide no register-robust boundary
corroboration at all** — the "one register stays boundary-clean" claim survives in **neither**
register. **The fork therefore rests entirely on the torus cells** (both registers LOOP-FILLING
under both statistics, §4). This is the honest and stronger statement.

The guard-dependence the earlier draft read as a "read-region artifact" tell was itself an
endpoint phase artifact: under the quiet-window mean the full-register CONCENTRATING is
guard-**insensitive** (g0/g1/g2 all CONCENTRATING, `guard_sensitive_qmean=False`) — it *meets* the
"genuine concentration is roughly guard-independent" criterion, not the cropping-artifact one.

**(2) The PML CONCENTRATING is boundary-DEPENDENT physics, not a read-region artifact.** Fixed
geometric-center **absolute** energies (33-site ball, drive-off → quiet-window average;
`_core_holding`, review MAJOR 2 — raw sums, immune to the CF/PR region-normalization):

| | PML `pair` | PML `graded_a0` | torus `pair` | torus `graded_a0` |
|---|---|---|---|---|
| core-ball E (drive-off → quiet-avg) | 0.611 → 0.920 (**+50.6 %**) | 0.673 → 0.963 (**+43.1 %**) | 0.351 → 0.265 (−24.4 %) | 0.392 → 0.284 (−27.6 %) |
| rest-of-interior E | 4.355 → 3.594 (−17.5 %) | 4.517 → 3.744 (−17.1 %) | +1.6 % | +1.9 % |
| near-sponge kinetic shells | −26.6 % | −26.8 % | 0 (no sponge) | 0 |
| H | −12.2 % | −12.2 % | −0.0 % (conserved) | −0.0 % |

Both knives fail. The **normalization-artifact** hypothesis is refuted — the CF rise is
numerator-driven (the core ball absolutely GAINS energy), not a shrinking denominator. The
**pure-drain** ("*looks* concentrated") reading is refuted too — periphery drain is real
(near-sponge kinetic shells lose ~−27 %) **AND** the central structure absolutely holds/gains
energy on the absorbing box. The plain reading: **the sponge removes the recirculating wake, and
the surviving central structure holds/gains absolute energy** while the interior drains and H
falls; on the same-seed torus the core disperses (−24 %) with H conserved. A **real
boundary-dependent core-holding signal, visible in both registers once phase-averaged** — not a
read-region artifact.

**SURFACED-NOT-INTERPRETED.** The numbers are reported and the signal is named a
*boundary-dependent core-holding* one; what it **means** (Reading-A wake-removal residue? a
distinct boundary effect?) is routed to Grant, not resolved here. It does **not** move the fork
(§7) — the fork is scored on the torus, where dispersal is robust under every read.

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
meter — read phase-robustly (§5) — the #689 boundary-**insensitivity** corroboration does not
survive. The #689 RESULT TL;DR item 2 —

> "The PML twins read the SAME sign (PR rises, CF falls → LOOP-FILLING under `pml=3` too)."

— held on the frozen **potential-only ENDPOINT** read. Under the phase-robust quiet-window mean
the PML twins read **CONCENTRATING in both registers** (§5), while the torus reads LOOP-FILLING.
Per §5:

- **Boundary-DEPENDENT physics, not a read-region artifact.** Phase-averaged, the fixed
  geom-center core ball absolutely **holds/gains** energy on the PML box (+50.6 % `pair`) while the
  interior drains (−17.5 %) and H falls (−12.2 %); the same-seed torus core disperses (−24.4 %)
  with H conserved. The sponge removes the recirculating wake; the surviving central structure
  holds its energy. A real **boundary-dependent core-holding signal** — surfaced; interpretation
  routed to Grant, **not** resolved here.
- **NOT register-robust corroboration.** Time-averaged, NEITHER register is boundary-insensitive
  (potential CONCENTRATING on the PML box vs LOOP-FILLING on the torus; full register likewise).
  The PML twins provide no register-robust boundary corroboration; **the fork rests entirely on
  the torus cells.**
- **NOT a revival of Reading B.** The fork is scored on the **torus** cells (no sponge); they read
  LOOP-FILLING on **both** registers under **both** statistics and are `guard_sensitive=False`.
  Dispersal is robust under every read. **The RULED Reading A is untouched.**

**G-PERSIST ★RULED firewall (explicit).** The ★RULED flip rests on the fork-independent PML
**φ-dispersion trend** — a reading of the **T2/Φ_link winding channel** (`Σ_port Phi_link²`, a
scalar gauge-accumulation ratio, [`k4_tlm.py:400`](../src/ave/core/k4_tlm.py)), a **different
meter** from the **A1** region-normalized energy-localization statistic and **never summed** with
it (A1 ⊥ T2). A boundary-dependent core-holding signal in the A1 energy meter therefore **cannot
structurally reach** the ★RULED basis: the two channels are measured on separate sectors, so
contamination of one does not propagate to the other. **G-PERSIST ★RULED is untouched.**

**What changes:** the boundary-**insensitivity** corroboration is **withdrawn** — it does not
survive the phase test in either register (the honest, stronger statement: the PML twins
corroborate nothing register-robustly; the fork stands on the torus). This is a
corroboration-level restatement for the auditor's manual/queue (**the auditor lands it**),
**not** a fork verdict change.

---

## 8 · KEEP-BOTH banking statement (formal)

- **BANKED (frozen) instrument — `energy_pot` (potential-only, interior mask):** the instrument
  of record for the **#689 run**. It is a correct read of the **potential** register; the #689
  RESULT §2 table is its provenance and is **NOT** edited or retracted by this addendum. It stays
  available (`BANKED_SECTOR="energy_pot"`) for reproduction of the historical read.
- **COMPLETED (forward) instrument — `energy_full` (potential + Cosserat kinetic, sponge-
  excluded):** the **MANDATORY** instrument for **all future meter use**, and **especially for
  any CONCENTRATING claim** — a concentration claim must be scored on the full register (both LC
  registers), with the **quiet-window-mean** phase-robust statistic as the PRIMARY read on the PML
  box (endpoint kept as a disclosed companion; review MAJOR 1), the two-statistic conjunction
  (`signature_conj`), the torus-native min-image CF ball, and the `guard_sensitive` / `nonmonotone`
  honesty flags. Potential-only or single-endpoint CONCENTRATING claims are **not** admissible
  going forward.
- **Plant scope (binding, from the #689 repair):** the two-meter (φ-plant + localization) combo is
  **un-foolable by DISTRIBUTED sustenance only.** The core-localized-pump adversary is the
  **required follow-on** named in the merged #689 RESULT and has **not** run — do **not** cite the
  combo as a general sustenance-proof detector until it does. The forward `--plant` on the
  completed instrument still reads `UN-FOOLABLE_CONFIRMED` for the distributed pump (φ sustained
  AND meter LOOP-FILLING).
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
