# α as boundary-energy partition, v2 — the (a3) RESERVOIR-EXCLUDED arm — PRE-REGISTRATION (frozen, committed alone)

**Date:** 2026-06-11
**Branch:** `analysis/2026-06-11-alpha-a3-reservoir` (off `origin/main` @ `f6ffd98d`)
**Route version:** **v2** of the α-boundary-energy-partition route. Predecessor (v1): branch
`analysis/2026-06-11-r1-alpha-forward-check` — prereg @ `cd7e7ae3`
(`research/2026-06-11_alpha-boundary-energy_prereg.md`), result @ `4f7ea648`
(`research/2026-06-11_alpha-boundary-energy_result.md`), PR #198 per dispatch (PR number from the
task dispatch; `gh` unreachable this session — network down; branch + SHAs verified locally via
`git show`). Per v1 result §7: *"any successor (e.g. … a re-extraction with the decoupled reservoir
properly accounted) gets its **own** version number and verification chain."* This is that successor,
with its own version + chain (Rule 12, KEEP-BOTH: the v1 docs are NOT edited).

**Predecessor verdict, verbatim (v1 result @ `4f7ea648`):**
> **VERDICT: DIFFERENT-RATIO (bin 2, §7).** … `r = 5.245763e-4` ; `r/ALPHA = 0.071886` (`r` is
> **~13.9× below α**) ; stationary **False** (drift `0.3093`) … `H_cons` (total conserved energy)
> carries the **canon-flagged decoupled-bulk reservoir** … The ONLY α-ward path (arm a3, exclude the
> decoupled reservoir) is **FENCED + ANALYTIC-BLOCKED**: the field is not banked, and excluding a
> reservoir to reach α is coincidence-magnet-adjacent — justified only by the `bulk_decoupled` flag,
> **never** by α-proximity. Not run.

This prereg runs exactly that fenced arm, under the fence's own terms: the exclusion criterion is the
**canon decoupling flag** (a dynamics property), defined and made executable **without reference to any
energy value** (§2), with the cross-object secondary promoted to a **GATE** (§7), the stationarity gate
inherited (§7), and the **NO-(a4) clause** committed verbatim (§7). Lane: implementer (orchestrated
dispatch; framing pre-adjudicated — this is prereg-v2 of the SAME route, not a new framing).

**Discipline tags applied:** `ave-prereg` (corpus-grep done — the only prior a3 work is the v1 fence
itself; no reservoir-excluded partition has ever been computed in the corpus), `verify-before-cite`
(every anchor re-grepped this session — §0.1), `ave-live-fire-derivation-provenance` (FORWARD-FIRST §5;
α dead-input as an EXECUTABLE grep gate, GATE-G), `consistency-vs-emergence` (§6),
`ave-apparatus-floor-attribution` (known-positive reproduction gate GATE-V — validate the bench on the
banked object before reading the new number), `ave-power-category-check` (inherited v1 §1.2 verbatim:
Q_reactive internal store-partition; unchanged by the exclusion — both numerator and denominator remain
reactive stores), `phase-space-coordinate-check` (inherited v1 §3.2: longitudinal/V-channel claim,
`E_V_cons` measurement — MATCHING), `substrate-native-check` (channel-ledger native; the exclusion is a
sector-membership statement on the K4/Cosserat channel ledger, not an energy heuristic),
`flag-don't-fix`, coincidence-magnet discipline (§0.2).

> **Status: PREREG — FROZEN. Not a result. Not canon.** Bins, tolerances, definitions, gates, and the
> NO-(a4) clause below are committed BEFORE any computation and are NOT to be re-opened post-hoc
> (the PARTITION-FREEZE LAW). This document is committed ALONE (Rule 11 / the v7 law).

---

## §0.1 — Verified anchors (verify-before-cite, re-grepped this session)

| # | Anchor | Status | Verbatim / value |
|---|---|---|---|
| 1 | v1 prereg arm (a3) definition, `cd7e7ae3:research/2026-06-11_alpha-boundary-energy_prereg.md` §3.3 | **VERIFIED** | `r3 = E_V_cons / (H_cons − E_bulk_decoupled)` — excludes the canon-flagged decoupled-bulk reservoir (`bulk_sector_unstable_free_evolution=True`, `bulk_decoupled_from_V_proof`) … "only justified by the bulk_decoupled flag, NEVER by α-proximity" |
| 2 | v1 result verdict + mechanism, `4f7ea648:research/2026-06-11_alpha-boundary-energy_result.md` | **VERIFIED** | quoted verbatim in the header above (DIFFERENT-RATIO; `r/ALPHA = 0.071886`; drift `0.3093`; a3 fenced+unbanked, not run) |
| 3 | banked MEASURED data — `s11_denovo_results.json` | **SHA-PINNED** | `570b50d7a560e54fb0c270a859e7e9c99c6e3968 : src/scripts/vol_9_device/_output/s11_denovo_results.json`; fields verified present this session: `made_build.{E_V_cons_first,E_V_cons_last,H_cons_first,H_cons_last,pocket_cells,bulk_sector_unstable_free_evolution,bulk_decoupled_from_V_proof}`; `planted` leg banks **probe-response only** (NO energy ledger — re-grep-confirmed: no `E_V_cons`/`H_cons` key anywhere under `planted`) |
| 4 | **FLAG-D** (the canon decoupling flag), `570b50d7:src/scripts/vol_9_device/s11_de_novo_sweep.py:636-658` + banked field | **VERIFIED** | `bulk_decoupled_from_V_proof = "V\|bulk-live - bulk-zeroed\|=0.0 over 8000 steps (V finite, decoupled)"`; code comment: "the V sector … and the omega carrier are EMPIRICALLY DECOUPLED from the bulk-density sector — the decouple test returned V\|bulk-live − bulk-zeroed\| = 0.000e+00 over 8000 steps (V identical, finite, even AFTER the bulk overflows)" |
| 5 | FLAG-D in the S11 result doc, `570b50d7:research/2026-06-11_s11-de-novo_result.md:63` | **VERIFIED** | "bulk sector, free evolution \| **unstable** (FLAG-D) \| ρ̄/u_adv overflow post-settle; **V decoupling proven**: V(bulk-live) − V(bulk-zeroed) = 0.0 over 8000 steps, V series finite throughout" |
| 6 | The H_total ledger decomposition, `570b50d7:src/ave/core/unified_genesis_engine.py:834-848` (`total_energy_unified`) | **VERIFIED** | `H = E_V_cons + shear_energy + omega_energy + _coupling_energy + bulk_kinetic_energy + bulk_internal_energy + snap_energy_ledger_total` (verbatim sum read from source this session) |
| 7 | Term implementations (all at `570b50d7`) | **VERIFIED** | `bulk_energy_conserved` `crystal_engine.py:380` (E_V: ½∫(∂ₜV)²/c_eff² + ½∫\|∇V\|²); `shear_energy` `crystal_engine.py:364` (w-sector); `omega_energy` `crystal_graft_v2.py:241` (ω-tank); `_coupling_energy` `crystal_graft_v4.py:174` (κ̃∫g·V·[w·(∇×ω)] — fields V,w,ω ONLY); `bulk_kinetic_energy` `unified_genesis_engine.py:1046` (½∫(1+ρ̄)\|u_adv\|²); `bulk_internal_energy` `unified_genesis_engine.py:817` (∫ε(ρ̄)dV); `snap_energy_ledger_total` `unified_genesis_engine.py:825` (snap-machine accumulators; `_snap_step` `:366` triggers on ρ̄≤ρ̄_cav — a bulk-density-sector machine) |
| 8 | α-token grep over the pinned engine closure | **VERIFIED (this session)** | `unified_genesis_engine.py, s11_probe_unified.py, crystal_engine.py, crystal_graft_v2/3/4.py, electron_spec_suite.py, genesis_v6_transducer_run.py` at `570b50d7`: **ZERO** matches for `ALPHA\|7.2973\|0.007297\|137.03`. `s11_de_novo_sweep.py`: exactly TWO α-touch lines — `:80` (`from ave.core.constants import ALPHA_COLD_INV`) and `:698-699` (post-hoc ringdown-Q note, *"post-hoc, NOT a bin criterion"*). This is the FROZEN allowlist for GATE-G (§5) |
| 9 | Determinism of the builders | **VERIFIED** | `build_made_probe` / `build_planted_probe` (`570b50d7:src/scripts/vol_9_device/s11_de_novo_sweep.py:105/140`) and their seed paths (`seed_lane1`, `seed_bulk`, `seed_omega_known_2_3`, `energize_rotation_column`, `freeze_wall_window`, `drive_chiral_photon`) contain **no RNG call** (grep `np.random\|default_rng`: zero hits in the engine closure; `np.random.seed(SEED)` exists only inside `genesis_v6_transducer_run` run-functions this driver never calls) → the made-leg re-run is reproducible against the bank (GATE-V) |
| 10 | `ALPHA` (CODATA) | **VERIFIED** | `src/ave/core/constants.py:133` = `7.2973525693e-3` (comparison target, loads LAST) |
| 11 | Two-α gap (corrected value) | **VERIFIED** | v1 result §6 flag-don't-fix catch: `\|ALPHA/ALPHA_COLD − 1\| = 2.2e-6` (~2 ppm, **6th digit** — the `constants.py:205` inline comment "≈7.29352e-3" is stale; the computed constant is correct). The two-α trap is therefore **maximally live**: at ANY forward band the two αs are indistinct |
| 12 | 2026-06-04 §5 gate law | **VERIFIED** | `research/2026-06-04_alpha-quarter-adversarial-rechallenge.md:54` (present at `f6ffd98d`, this branch): "over-determination is the **tell of a coincidence-magnet** … evidence *only* if a route made a **discriminating secondary prediction** … **and the substrate confirmed THAT**" |

**Glimpse disclosure (freeze-integrity):** the banked scalars `E_V_cons_last ≈ 12.91`, `H_cons_last ≈
24612` and the v1 ratio `r = 5.2458e-4` are public on the v1 branch and were read this session. **No
sector-resolved value (E_w, E_ω, H_couple, bulk-KE, bulk-U — for either object) exists anywhere in the
corpus** (grep-receipt: the banked JSON has no such field; no other JSON banks them). The frozen
quantity `r_a3` is therefore **not computable from anything seen before this freeze** — for either
object. The planted object's energy ledger has **never been measured at all**.

## §0.2 — The two-α trap (inherited, with the v1 §6 correction)

The comparison TARGET is CODATA `ALPHA` (`constants.py:133`). The golden-torus geometric
`ALPHA_COLD = 1/(4π³+π²+π)` agrees with it to **~2 ppm** (anchor #11) — so NO forward energy-partition
band can distinguish "matches CODATA α" from "reconstructs the golden-torus geometric α". Inherited
consequence (v1 §0.2, unchanged): a measured match is at best **emergence-CANDIDATE**, never a
golden-torus discriminator; the analytic golden-torus path **STAYS blocked** (§1).

---

## §1 — THE FENCE (carried over from v1 — the §5 gate law ran FIRST there; verdict inherited)

Per the dispatch and the 2026-06-04 §5 gate law, the v1 fence verdict **carries over verbatim**:

- **MEASURED arm: ORTHOGONAL** to all four closed α routes (kinematic-bijection lift /
  ¼-reconstruction family / Nyquist-binding #192 / radiation-ladder) — v1 §1.1 table, unchanged. The
  v2 measurement is the SAME move (a conserved-energy ratio measured on self-assembled objects) with a
  canon-flagged sector excluded by a **dynamics criterion** (§2); it introduces no geometric lift, no
  sampling-rate identity, no flux ladder, no geometric count.
- **ANALYTIC arm: STAYS BLOCKED.** The analytic golden-torus path (wall-energy integral reachable only
  via `Q = 4π³+π²+π`) was fenced in v1 §1.1/§4.1 and binned ANALYTIC-BLOCKED in v1 result §3. **No new
  analytic primitive is banked; v2 does NOT run an analytic arm.** The route stands or dies on the
  MEASURED arm.
- The a3-specific fence condition (v1 §3.3/§8: *"justified only by the bulk_decoupled flag, NEVER by
  α-proximity"*) is DISCHARGED by construction in §2: the exclusion criterion is committed here, before
  any computation, defined purely by sector-membership under the FLAG-D decoupling proof, and made
  executable with **zero reference to any energy value**.

## §2 — THE EXCLUSION CRITERION (Protection 1: value-blind, canon-flag-selected)

**Criterion C (frozen):** a term of the `total_energy_unified` ledger is **EXCLUDED** (belongs to the
decoupled reservoir `E_resv`) **iff it is a functional only of the bulk-density-sector state — the
exact sector the FLAG-D decoupling proof zeroes** (`bulk_decoupled_from_V_proof`, anchors #4/#5: the
proof zeroed `ρ̄`/`u_adv` [the "bulk-zeroed" leg] and found V identical over 8000 steps). Membership is
decided by **which fields the term reads**, never by its value:

| Ledger term (anchor #7) | Fields read | Zeroed by the FLAG-D proof? | Verdict |
|---|---|---|---|
| `bulk_energy_conserved` (E_V) | V, ∂ₜV, c_eff(V) | no | **LIVE** (the numerator channel) |
| `shear_energy` (E_w) | w, ∂ₜw | no | **LIVE** |
| `omega_energy` (E_ω) | ω, ∂ₜω | no | **LIVE** |
| `_coupling_energy` (H_couple) | V, w, ω (κ̃∫g·V·[w·(∇×ω)]) | no | **LIVE** |
| `bulk_kinetic_energy` | ρ̄, u_adv (½∫(1+ρ̄)\|u_adv\|²) | **yes** | **EXCLUDED** |
| `bulk_internal_energy` | ρ̄ (∫ε(ρ̄)dV) | **yes** | **EXCLUDED** |
| `snap_energy_ledger_total` | snap accumulators; sourced solely by `_snap_step`, which fires on ρ̄≤ρ̄_cav (a bulk-density-sector machine, anchor #7) | **yes** (machine can never fire with ρ̄≡0; banked `pocket_cells=0` besides) | **EXCLUDED** |

**FROZEN ledgers:**
```
E_resv ≡ bulk_kinetic_energy + bulk_internal_energy + snap_energy_ledger_total
E_live ≡ E_V_cons + E_w + E_ω + H_couple        (computed DIRECTLY as this sum)
```
`E_live = H_cons − E_resv` algebraically (anchor #6); it is computed directly because FLAG-D warns the
reservoir can overflow to non-finite under free evolution — the live ledger stays finite and
well-defined exactly because it is the decoupled complement.

**Executable, value-blind selection gate (GATE-X — the prereg's "show the criterion selects the
excluded ledger WITHOUT reference to any energy value", made code):** on a deep-copied engine state,
set `rho_bar[:] = 0`, `u_adv[:] = 0` (the FLAG-D "bulk-zeroed" operation, verbatim). Then assert:
- every **EXCLUDED** term evaluates to **exactly 0.0** on the zero-clone (and the snap accumulators are
  identically zero on these objects, consistent with banked `pocket_cells = 0`);
- every **LIVE** term is **bit-unchanged** between the original and the zero-clone.
The partition is thereby selected by the decoupling **dynamics** (which fields the proof zeroes), with
no energy value anywhere in the selection. GATE-X failure ⇒ bin NEEDS-RERUN (criterion-selection
failure named).

**Ledger-closure gate (GATE-L):** at every recorded sample where all terms are finite,
`|(E_live + E_resv) − H_cons| ≤ 1e-9·|H_cons|` (the decomposition must reproduce the banked total
exactly — anchor #6 is a sum, not a model).

## §3 — FROZEN PRIMARY + objects

```
r_a3(X) ≡ E_V_cons(X) / E_live(X)
```
evaluated at the **last build-window sample** (s = N_BUILD = 3200; mirrors the banked `_last`
convention), for BOTH objects:

- **X = MADE** — the de-novo MAIN object: `build_made_probe(G.make_cfg("MAIN", helicity=1),
  drive_sector="V", drive_amp=0.0, src_sigma=2.5)` — byte-pinned builder (anchor #9), the SAME call the
  banked leg ran.
- **X = PLANTED** — the #166-style planted article in the SAME engine config:
  `build_planted_probe(cfg)` — byte-pinned. Its conserved-energy ledger is measured here for the
  first time (the v1 §2 "one cheap re-extraction", now a frozen protocol §4).

Definition lineage: this is v1 arm (a3) with the unbanked field `E_bulk_decoupled` instantiated as
`E_resv` by Criterion C, i.e. `r_a3 = E_V_cons/(H_cons − E_resv)`, computed in the direct-sum form.

## §4 — RE-EXTRACTION protocol (frozen; "a small re-run, NOT a new physics sim" — v1 §2)

Engine code is **materialized at the pinned SHA** (`git show 570b50d7:<path>`) into an isolated import
root; the driver asserts at runtime that every imported engine module's `__file__` resolves inside that
root (no drift to the branch's own `src/`). FAST mode is refused (`S11_FAST` must be unset).

- **MADE leg (verbatim banked recipe + ledger recording):** build N_BUILD=3200 steps recording the full
  7-term ledger at s=0 and every REC=200; then the banked drive-off (`drive_helicity=0; w[:]=0;
  w_prev[:]=0`); then N_SETTLE=2200 settle steps recording every 200.
  **GATE-V (known-positive reproduction; ave-apparatus-floor-attribution):** the re-run must reproduce
  the banked `E_V_cons_first/last`, `H_cons_first/last` to **rel ≤ 1e-9** and `pocket_cells == 0`
  exactly, and `spec_T1_mass_converges(E_V series)` must bin CONVERGED — else **NEEDS-RERUN
  (apparatus non-reproducibility named)**: the bench failed its known cap and no new number is read.
- **PLANTED leg (same instrument, same schedule):** evolve 3200 steps recording every 200 (its "build
  window" — the planted article starts assembled and relaxes), then 2200 further free steps recording
  every 200 (its settle window). **No drive-off mutation is applied** (the planted object has no
  chiral-photon drive to switch off; zeroing its buckle-grown `w` mid-run would mutate the object —
  protocol-fidelity note, frozen here). Finiteness of the LIVE ledger is required at every sample;
  a non-finite live-ledger sample ⇒ NEEDS-RERUN (named). A non-finite RESERVOIR sample is expected
  under FLAG-D, reported, and does not block (the live ledger is its decoupled complement).

## §5 — FORWARD-FIRST protocol (ave-live-fire-derivation-provenance; α loads LAST)

Driver order (frozen):
1. **GATE-G — the executable α-dead-input grep gate (runs FIRST, before any engine import and before
   any `ave.core.constants` import):** scan the materialized pinned sources. Assert: ZERO matches for
   `ALPHA|7\.2973|0\.007297|137\.03` in the engine closure (anchor #8 list); exactly the two
   allowlisted α-touch lines in `s11_de_novo_sweep.py` (`:80` import, `:698-699` post-hoc note);
   the AST source of `build_made_probe`/`build_planted_probe` contains no α token; the driver's own
   source ABOVE its `# == ALPHA-LOAD-MARKER ==` line contains no α token or CODATA literal. Any
   failure ⇒ abort (no run).
2. Run §4 (both legs). Print the full per-sample ledgers.
3. **PRINT both objects' `r_a3`**, the stationarity drifts, GATE-V/X/L results, and the cross-object
   spread — **all before α is referenced**.
4. `# == ALPHA-LOAD-MARKER ==` — THEN `from ave.core.constants import ALPHA`; compute and print
   `r_a3/α` per object and evaluate the frozen bins (§7).

## §6 — consistency-vs-emergence (pre-committed)

α is a **DEAD input by construction** to both legs (GATE-G makes the v1 result §4 static finding
executable). Therefore:
- **bin 1 (MATCHES-α) ⇒ emergence-CANDIDATE class** — a measured, cross-object-invariant,
  stationary, α-free-input partition equal to α within the coarse band. It would license EXACTLY: (i)
  a registered candidate row (candidate, NOT canon — the coarse band cannot beat the 2-ppm two-α trap,
  §0.2), and (ii) a successor *derivation-target* prereg (parameter-free wall-energy integral, still
  fenced against the golden-torus count). It would NOT license: any constants.py change, any manuscript
  α-claim, any "α derived" language, anywhere.
- **bins 2/3** ⇒ nothing to class (no match), and the route closes (§7).

## §7 — FROZEN BINS (ordered) + EXECUTABLE GATES + THE NO-(a4) CLAUSE

Frozen tolerances (inherited where they existed; committed before computation):
```
TOL_MATCH  = 0.25      # per-object: |r_a3/ALPHA − 1| ≤ 0.25  (coarse forward band, v1 §7)
TOL_TIGHT  = 0.05      # tight sub-flag (v1 §7)
TOL_SPREAD = 0.25      # cross-object: |r_a3(made)/r_a3(planted) − 1| ≤ 0.25 (frozen here)
TOL_DRIFT  = 0.10      # stationarity, inherited v1 band: per-object SETTLE-window drift
                       #   |r_a3(settle end)/r_a3(settle start) − 1| ≤ 0.10
```
Stationarity window declaration (frozen, with reasoning): the gate runs on the **settle window** (the
converged free object — what "structural fraction" means; the v1 gate's t=0 endpoint is the seeded
initial condition, pre-assembly). The v1-verbatim companion (build-window first→last drift) is
**reported alongside** for continuity but is not the gate. Committed before any computation; the
panel checks this freeze.

**Ordered bins:**
1. **MATCHES-α** — fires **ONLY IF ALL of**: GATE-G, GATE-V, GATE-X, GATE-L pass; **BOTH** objects
   satisfy `|r_a3/ALPHA − 1| ≤ TOL_MATCH`; the cross-object spread satisfies `TOL_SPREAD`; **BOTH**
   objects satisfy `TOL_DRIFT`. (Protection 2: the cross-object secondary is a **GATE**, not a check —
   **one-object matches are SCALE-ACCIDENT by definition**.) Class per §6: emergence-CANDIDATE.
2. **SCALE-ACCIDENT** — at least one object inside `TOL_MATCH` but bin-1 fails (one-object-only match,
   or spread-fail, or stationarity-fail on a matching object). **Consequence (frozen): the route
   closes** — a non-structural, object-particular coincidence is exactly what the §5 gate law's
   secondary exists to expose; no successor partition will be pre-registered.
3. **DIFFERENT-RATIO** — neither object inside `TOL_MATCH`. Report `r_a3/α` per object and what the
   live-share physically is.
4. **NEEDS-RERUN** — GATE-V, GATE-X, or GATE-L fails, or a live-ledger sample is non-finite: the named
   blocker is reported; **no physics bin is assigned** and the honest cost report states what a clean
   rerun needs.

**THE NO-(a4) CLAUSE (frozen verbatim, per dispatch):** "if this bins DIFFERENT-RATIO, the
boundary-energy route is FULLY DEAD — no successor partition will be pre-registered." Scope note
(frozen): bin 2 (SCALE-ACCIDENT) carries the same no-successor consequence by its own §5-gate-law
logic; bin 4 (NEEDS-RERUN) does NOT trigger the clause (an apparatus failure is not a physics negative
— regime-discipline: a null where the measurement could not run is an artifact, not a falsification).

**Executable gate sketch (Phase-2 implements verbatim):**
```python
# GATE-G (before any engine/constants import): allowlisted alpha-grep over pinned sources — §5.1
# run made leg + planted leg (§4); ledgers recorded
ra3_made    = EV_made_build_last    / Elive_made_build_last      # FROZEN primary, made
ra3_planted = EV_planted_build_last / Elive_planted_build_last   # FROZEN primary, planted
drift_made    = abs(ra3_made_settle_end    / ra3_made_settle_start    - 1.0)   # ≤ 0.10
drift_planted = abs(ra3_planted_settle_end / ra3_planted_settle_start - 1.0)   # ≤ 0.10
spread        = abs(ra3_made / ra3_planted - 1.0)                              # ≤ 0.25
# print ALL of the above, THEN:
# == ALPHA-LOAD-MARKER ==
from ave.core.constants import ALPHA
match_made    = abs(ra3_made    / ALPHA - 1.0) <= 0.25
match_planted = abs(ra3_planted / ALPHA - 1.0) <= 0.25
bin1 = (gates_GVXL_pass and match_made and match_planted
        and spread <= 0.25 and drift_made <= 0.10 and drift_planted <= 0.10)
```

## §8 — Step-3.5 dimensional / magnitude pre-registration (ave-prereg v1.1)

`r_a3` is dimensionless (energy/energy), bounded in `(r_v1, 1]` per object where `r_v1 = 5.25e-4`
(removing a non-negative reservoir from the denominator can only raise the share). The live denominator
`E_live = E_V + E_w + E_ω + H_couple` is **unbanked for both objects** — no sector-resolved energy has
ever been extracted (§0.1 glimpse disclosure), so this is a genuinely forward number with real teeth:
- `r_a3 = α` requires `E_live ≈ E_V/α ≈ 137·E_V` — i.e. the live ω/w/coupling stores would have to
  carry ≈ 136× the longitudinal store. **No canonical leaf pins that ratio**; nothing in the corpus
  predicts it.
- **Pre-registered most-probable outcome (honest):** **DIFFERENT-RATIO** — with the reservoir excluded,
  the a-priori-likely live ledger is dominated by either E_V itself (`r_a3 → O(1)`, ~137× ABOVE α) or
  by the ω-tank at some unpinned ratio; landing inside [0.75α, 1.25α] on BOTH objects AND agreeing to
  25% AND stationary to 10% would be a four-coincidence stack with no registered mechanism. The route
  is being given its best shot precisely so that a negative is FULLY load-bearing (the NO-(a4) clause).
- Per-object overshoot direction is informative and will be reported: `r_a3 ≫ α` says the boundary
  store dominates its own live complement (the turns-ratio picture inverts); `r_a3 ≪ α` says the live
  complement still dwarfs the boundary store even without the reservoir.

**Cost registration:** N=48³ engine, 5400 recorded steps per leg + ledger evaluations every 200 steps
(7 functional evaluations per sample) + one GATE-X zero-clone per leg — estimated minutes-scale per leg
on this machine (the banked full sweep, including 24000-step ringdowns and 20-point windows, took
3110 s). If a leg exceeds ~30 min it is killed and binned NEEDS-RERUN with the measured cost.
