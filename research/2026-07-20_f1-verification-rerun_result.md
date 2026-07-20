# F1 (coupled K4↔Cosserat) verification refire — reproduction gate on current main

**Date:** 2026-07-20 · **Branch:** `research/f1-verification-rerun` (worktree off `origin/main` @ `e2e870c0`) ·
**Class:** reproduction gate (the #746 class — convert "probably still true" into "reproduced on
today's engine"). **No new physics. No chord. Additions-only (this doc + one JSON receipt); zero
engine edits.** · **Consistency-class** (`consistency-vs-emergence`: this re-runs banked drivers and
compares receipts; it does not derive or emerge anything).

**What "F1" means here** (verify-before-cite; distinct from the capability-map "F1 ruling" on the
`S^0.5` exponent defect): the **F1 DEFECT fix (Grant 2026-07-15)** — `external_z_local` on
`K4Lattice3D`, set `True` under `CoupledK4Cosserat`, so the Cosserat↔V shared front `√(S_μ/S_ε)`
survives `k4.step()` and reaches bond Γ (`k4_tlm.py:168–177,187–189,324–329`;
`k4_cosserat_coupling.py:309,872`). Commits: `79435ee3` (fix + `test_f1_shared_front_ordering.py`),
`20395fe2` (S_field-advance follow-up). Both are ancestors of the audited HEAD.

**Provenance of the battery + the banked receipts** (the F1 lane's own scheduling docs):
[`2026-07-16_f1-v-active-consumer-audit_NOTE.md`](2026-07-16_f1-v-active-consumer-audit_NOTE.md),
[`2026-07-16_f1-materiality-report_NOTE.md`](2026-07-16_f1-materiality-report_NOTE.md). The battery is
**scattered, not a single suite** — it is (a) the F1-path regression + coupled tests and (b) the three
materiality-flagged gated re-runs, in the report's priority order. This doc enumerates honestly and
re-runs the banked-receipt cells it could locate; a NOT-RERUN list carries the rest.

**Discipline:** Rule-11 (banked receipts compared, never edited; drift → both banked); flag-don't-fix
(contradictions surfaced, not resolved); seeds/configs matched to the banked runs.

---

## TL;DR (brutal-clarity)

1. **★GENESIS-NODE-BIRTH (priority-1, Grant-ordered first) — REPRODUCES.** The F1-materiality-critical
   quantity `v_inc_peak` (the V-spatial peak the D1–D4 gates read) is **bit-stable to every banked
   digit** across all three landed seed modes, at BOTH fidelities. `E_persist`, `rank4`, per-leg
   persist verdicts, and the frozen bin — **smoke `i_A_SUPPORTED`, production `ii_A_WEAKENED`** —
   all reproduce. The priority-1 flip risk the materiality report flagged (a sub-% `v_inc_peak` shift
   crossing a D1–D4 gate) **did NOT materialize**.
2. **One disclosed, verdict-invariant DRIFT:** the `pair` smoke `φ_persist` (`Φ_link` weak-spatial
   channel) moved **7.7295 → 7.2323 (−6.4 %)**; it stays far above the 0.80 gate floor, so the PASS
   verdict is unchanged. At production the same channel drifts ≤0.33 %. `graded_a0` φ is essentially
   unmoved (Δ ≤ 0.02 %). Banked BOTH; routed to Grant (Rule-11 / flag-don't-fix).
3. **Genesis-24 (priority-2) — QUALITATIVE VERDICT `C1` REPRODUCES; QUANTITATIVE `dE_V` DRIFTS
   (F1-attributable, +10.8…+42.2 %).** The pre-step seed peaks and the photon-OFF control arm are
   bit-identical; only the photon-ON V-active arm (whose bond-Γ the F1 shared-front now sets) moves
   (+0.4 % E_V), amplified through the `dE_V` difference. The banked JSON is the corrected `−2`
   Lenz C1 (not the superseded `+2`-bug runaway). This is the materiality report's exact row-2
   prediction, now measured. Banked BOTH (Rule-11). See §Contradictions for the report's stale citation.
4. **F1-path regression + coupled/cross-sector/genesis/gpersist-ontology tests — all GREEN on
   current main** (55 tests). `make verify` green.
5. **CONTRADICTION FLAGGED (not fixed):** the materiality report's genesis-24 row cites the
   superseded `+2`-bug numbers (`max|V_inc|→1.08e4`, VERDICT B), which the 2026-06-21 Lenz correction
   replaced 26 days earlier with the bounded `−2` C1 (`max|V_inc|~0.37`). See §Contradictions.

---

## Battery enumeration (honest; verify-before-cite)

The F1 battery is **scattered** across pytest regressions and three driver re-runs. Enumerated:

| # | Cell | Kind | Banked receipt | Re-ran? |
|---|---|---|---|---|
| R1 | `test_f1_shared_front_ordering.py` (7) | pytest regression (direct F1-path) | in-test asserts | ✅ PASS |
| R2 | `test_scalar_grade_seed_f1.py` (3) | pytest regression (F1 scalar-grade seed) | in-test asserts | ✅ PASS |
| R3 | `test_coupled_eigensolve.py` + `test_coupled_resonator.py` + `test_cross_sector_coupling.py` + `test_genesis_node_birth_discriminator.py` (fast keepers) + `test_gpersist_meter_ontology.py` (45) | pytest (coupled K4↔Cosserat host) | in-test asserts | ✅ PASS |
| **P1★** | `genesis_node_birth_discriminator.py` | **driver — priority-1 flip risk (v_inc_peak→D1–D4 gates)** | [`…genesis-node-birth-discriminator_result.md`](2026-07-12_genesis-node-birth-discriminator_result.md) tables (in-doc; no separate JSON) | ✅ **smoke + production** |
| P2 | `genesis_24_saturated_seed.py` | driver — priority-2 (pumped runaway, quantitative `max|V_inc|`) | `src/scripts/vol_1_foundations/genesis_24_saturated_seed_results.json` (banked 2026-06-21, **pre-F1**) | ✅ full |
| P3 | `gpersist_localization_observable.py` | driver — priority-3 (confirmation only; localization meter = the exact V-spatial class the fix touches) | [`…gpersist-localization-observable_RESULT.md`](2026-07-14_gpersist-localization-observable_RESULT.md) §5 receipts | ⏳ see NOT-RERUN §c |

**Banked-receipt provenance note.** The genesis-node-birth cell has **no separate JSON receipt** — its
banked receipt is the D2 battery table inside the 2026-07-12 result doc (smoke + production + domain
sweep). The genesis-24 cell has a serialized in-tree JSON (`…_results.json`); Rule-11 forbids editing it,
so the re-run's output was captured to scratch and the in-tree file restored (`git checkout`) — this doc
adds **no** engine/JSON edits.

## Per-cell MATCH / DRIFT

### ★P1 — genesis-node-birth discriminator (priority-1, Grant-ordered first)

Banked config unchanged: `run_loop_gap_probe(N=10, rank_target=4, bulk_density_on=True,
front_target=A_YIELD, n_drive_mult=0.5, n_quiet_mult=1.5)`, all three landed seed modes, both
fidelities. Persist gate (frozen): `E_persist ≥ 0.85 AND φ_persist ≥ 0.80`. Banked values from the
2026-07-12 result-doc D2 tables (:132–134 smoke, :149–151 production).

**SMOKE (`fast=True`) — bin `i_A_SUPPORTED` reproduced**

| seed | E_persist (bank→rerun) | φ_persist (bank→rerun) | rank4 | **v_inc_peak** (bank→rerun) | persist | verdict |
|---|---|---|---|---|---|---|
| `pair` | 0.8639 → 0.863903 | 7.7295 → **7.2323** | T→T | 0.0122 → 0.012192 | PASS→PASS | **DRIFT** (φ −6.4 %, verdict-invariant) |
| `photon_lock` | 0.8198 → 0.819784 | 0.0000 → 0.0000 | F→F | 0.0000 → 0.0000 | FAIL→FAIL | MATCH |
| `graded_a0` | 0.8544 → 0.854407 | 1.9636 → 1.963773 | T→T | 0.0188 → 0.018824 | PASS→PASS | MATCH |

**PRODUCTION (`fast=False`) — bin `ii_A_WEAKENED` reproduced**

| seed | E_persist (bank→rerun) | φ_persist (bank→rerun) | rank4 | **v_inc_peak** (bank→rerun) | persist | verdict |
|---|---|---|---|---|---|---|
| `pair` | 0.6929 → 0.692889 | 0.8734 → 0.870536 | F→F | 0.0122 → 0.012192 | FAIL→FAIL | MATCH (φ −0.33 %) |
| `photon_lock` | 0.7750 → 0.774952 | 0.0000 → 0.0000 | F→F | 0.0000 → 0.0000 | FAIL→FAIL | MATCH |
| `graded_a0` | 0.6764 → 0.676390 | 0.8905 → 0.890792 | F→F | 0.0188 → 0.018824 | FAIL→FAIL | MATCH (φ +0.03 %) |

**D1 (both fidelities):** crystal_engine 4096→4096, master_equation_fdtd 4096→4096 (measured, 40
steps), loop_gap_harness 1000 structural — **MATCH** (2 measured + 1 structural, invariant).

**Read (not interpreted).** `v_inc_peak` — the quantity the materiality report flagged as the *only*
threshold-gate-on-a-V-spatial-peak, "highest flip risk" — is identical to every banked digit at both
fidelities. `E_persist` and `rank4` reproduce to 4 dp. Both frozen bins reproduce. The lone movement
is `φ_persist` on the `pair` seed at smoke (−6.4 %); the F1 fix landed 2026-07-15, **after** the
2026-07-12 banked run, and `Φ_link` is the weak-spatial channel the fix's spatial re-routing can move
(consumer audit §3b), so this drift is consistent with the F1 fix — but it is **verdict-invariant**
(7.23 ≫ 0.80 floor). Banked BOTH; routed to Grant.

### P2 — genesis-24 saturated-seed (priority-2, banked JSON pre-F1 by 24 days)

Config = banked (`N=24, steps=40, emit=60`). Banked receipt = `…_results.json` (the `−2` Lenz C1,
banked 2026-06-21; F1 fix landed 2026-07-15). Compared field-by-field (banked scratch copy vs re-run;
in-tree file restored after).

**Qualitative verdict + topology — MATCH (invariant):**

| field | banked → rerun |
|---|---|
| `verdict` | **C1** → **C1** |
| `headline_monotone` / `deep_positive` | False/False → False/False |
| `seed_audit.max_V_inc` (all 4 fracs) | **bit-identical** (0.11563155 / 0.23126311 / 0.32762274 / 0.36616659) |
| `seed_audit.E_V_seed` (all 4 fracs) | bit-identical |
| `smoke.E_V_arm2` (control, photon-OFF) | 5.901349 → **5.901349** (identical) |
| `arm2_topology_null` / `arm4_charge_flip.any_flip` | True/True → True/True |
| `ledger.L_bounded` / `emission_reverse.reverses` | False/True → False/True |
| `seed_audit_all_admissible` / `forbidden_seeder_used` | True/[] → True/[] |

**Quantitative `dE_V` headline — DRIFT (F1-attributable):**

| frac | dE_V banked → rerun | rel Δ |
|---|---|---|
| 0.3 | −0.010094 → −0.005836 | **+42.2 %** |
| 0.6 | −0.064000 → −0.048685 | **+23.9 %** |
| 0.85 | −0.170550 → −0.147318 | **+13.6 %** |
| 0.95 | −0.238724 → −0.212998 | **+10.8 %** |

**Read (not interpreted).** The **pre-step** quantities (seed peaks, seed energy) and the **photon-OFF
control arm** are bit-identical — correctly, since seeds are direct-write and F1 only re-routes during
scatter. The drift is confined to the **photon-ON arm-1** (`E_V_arm1` 5.730800 → 5.754031, +0.4 %),
which is the V-active + Cosserat-active leg whose bond-Γ the shared-front fix now sets. `dE_V` is a
**difference** of two ~5.9 quantities, so a +0.4 % arm-1 gain amplifies to a +10.8…+42.2 % relative
`dE_V` shift (largest where |dE_V| is smallest). **The verdict C1 is invariant** (`dE_V` stays
`≤ eps_machine` at deep saturation on every frac) and every topological flag is invariant. This is
exactly the materiality report's row-2 prediction — *quantitative peak may shift, qualitative FIRES
robust* — now measured, not assumed. Banked BOTH; Grant adjudicates whether the banked JSON is
refreshed to the post-F1 `dE_V` values (a receipt-refresh call, out of this lane's scope).

### R1–R3 — F1-path regression + coupled/cross-sector/genesis/gpersist-ontology tests

All GREEN on current main (worktree `src/`):

| suite | tests | result |
|---|---|---|
| `test_f1_shared_front_ordering.py` (incl. `TestF1MaterialityKernel`: 1.045-class survives, power-conservation E_V-invariant, Cosserat-quiet identity) | 7 | PASS |
| `test_scalar_grade_seed_f1.py` | 3 | PASS |
| `test_coupled_eigensolve.py` + `test_coupled_resonator.py` + `test_cross_sector_coupling.py` + `test_genesis_node_birth_discriminator.py` (fast keepers) + `test_gpersist_meter_ontology.py` | 45 | PASS |

These exercise the F1 code path directly (`external_z_local` set + honored, shared front survives
`k4.step()`, power-conserving E_V invariance, S_field still advances) and the coupled-host spectra.

## Deviations

- **Seeds/configs matched to the banked runs.** genesis-node-birth: banked `run_loop_gap_probe`
  knobs unchanged (N=10, rank 4, bulk on, front=A_YIELD, drive/quiet mults 0.5/1.5), both fidelities,
  all three landed seed modes. genesis-24: driver defaults = banked config (`N=24, steps=40,
  emit=60`, per the JSON `config` block). No unmatchable parameter. The engine is **deterministic**
  (E_persist and v_inc_peak reproduce to ≥4 dp with no RNG jitter), so drifts are real engine
  differences between the banked commit and current HEAD, not run-to-run noise.
- **genesis-24 in-tree JSON restored.** The driver writes its receipt to a hardcoded in-tree path;
  Rule-11 forbids editing the banked receipt, so the re-run output was diffed against a scratch copy
  and the tracked file restored via `git checkout` — this branch adds no engine/JSON change.
- **Environment:** worktree off `origin/main` @ `e2e870c0`; shared main `.venv`; `PYTHONPATH`
  pinned to the worktree `src/` (worktree-aware local-validation discipline).

## Contradictions (flag-don't-fix)

**C1 — the materiality report's genesis-24 row cites a superseded regime.** Both F1-lane scheduling
docs characterize genesis-24 as a *pumped runaway*:

- `2026-07-16_f1-materiality-report_NOTE.md:24` — "`max|V_inc|→1.08e4`; source-channel-FIRES
  (VERDICT B) … **pumped runaway** (converter on → E_V not conserved)"; `:35`, `:49` repeat "pumped
  runaway".
- `2026-07-16_f1-v-active-consumer-audit_NOTE.md:180` — "V-active (**runaway →1e4**)"; `:120–121`
  "the runaway/pumped regime (genesis-24, 1e4 V-growth)".

But the **current banked receipt** — `genesis_24_saturated_seed_results.json`, regenerated **2026-06-21**
by the Lenz-sign correction (`5a8b16e3`), **26 days BEFORE** those reports — is the **bounded, power-
conserving `−2` C1**: `verdict = "C1"`, `dE_V` all-negative (`0.85: −0.1705`), `max_V_inc ≈ 0.37`
(not `1.08e4`). The genesis-24 result doc's own CORRECTING HEADER reconciles this
(`2026-06-09_genesis-24-saturated-seed_result.md:80–88`): under the corrected `−2` EMF sign the source
REVERSES, there is no runaway, and the deep-saturation gate reads **C1**; the `1.08e4` / `6.8e8` /
VERDICT-B runaway is the superseded `+2`-BUG (result-doc `:73`, `:296–297`, preserved Rule-12).

**Direction of the error:** the report over-states genesis-24's F1 flip-risk — a *bounded C1* is the
power-conserving regime the audit §3b proves `E_V`-invariant, i.e. LESS spatially flip-prone than the
runaway the report assumed, not more. So the materiality *conclusion direction* (genesis-24 qualitative
verdict robust to F1) is unharmed; only the **cited receipt is stale**. Not edited here (flag-don't-fix;
report-class docs, auditor/Grant adjudicates). This re-run compares against the **live banked JSON**
(the `−2` C1), which is the correct receipt.

## NOT-RERUN list (with reason)

**(a) genesis-node-birth domain-size sweep (N=12, N=14; `pair` production).** Banked
`E_persist = 0.7984 / 0.8449` (result-doc `:191–193`). NOT-RERUN: this is a **boundary-leakage
diagnostic** (E_persist vs domain size, energy-class), **not** the F1-material V-spatial-peak question.
The F1-critical N=10 anchor (`E=0.692889`, `v_inc_peak=0.012192`) reproduced exactly above, and
`E_persist` is §3b-invariant to the F1 fix (power-conserving bond reflection). ~18 min for 2 points;
deferred to keep the deliverable bounded. If Grant wants the boundary-recovery trend re-confirmed on
today's engine, it is a cheap follow-on.

**(b) gpersist-localization-observable (P3, priority-3 confirmation-only).** Banked receipts:
`…gpersist-localization-observable_RESULT.md` §5 (torus `pair` φ=10.5197 / `graded_a0` φ=10.4218;
PR 348.7→491.6; CF 0.062→0.052; LOOP-FILLING ⇒ Reading A). NOT-RERUN in this refire: it is the
**heaviest cell** (4 production torus/PML cells + φ-channel plants, ≳30 min) and is explicitly
**confirmation-only, do-NOT-reopen G-PERSIST ★RULED** (materiality report `:38–39`). Its localization
meter *is* the exact V-spatial class the F1 fix touches — but the **highest-flip-risk** member of that
class (genesis-node-birth `v_inc_peak`) already reproduced bit-stable above, so the confirmation value
here is marginal against its cost. `test_gpersist_meter_ontology.py` (its meter-ontology regression)
**did** re-run GREEN (R3). Flagged as the natural next-free re-run if Grant wants the localization
statistic itself re-confirmed on current main.

**(c) The three mechanism-robust consumers the materiality report did NOT flag** (report `:41–43`):
- `2026-07-13_genesis-npersist-n14-battery_RESULT.md` — **energy-class** (E-persist), §3b-invariant to
  the fix.
- `2026-06-04_full-electron-option-B-discrete-emergence-result.md` — heavy prior adjudication already
  corrects driver auto-verdicts; low priority.
- `2026-06-09_cross-sector-pump-confirmation_result.md` — the channel reads `V_sq`/converter force,
  **not** `z_local`; the null is z_local-independent → robust by construction.

**(d) The 13 non-coupled-engine + coupled-eigenmode (`.step()`=0) consumers** — N/A to the F1 ordering
(consumer audit §5.1); not part of the reproduction battery.
