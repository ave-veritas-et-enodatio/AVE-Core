# RESULT — Annihilation / Evaporation Phase-2 run (the reverse reaction of the condensation ontology)

**Date:** 2026-06-11
**Prereg:** `research/2026-06-11_annihilation-evaporation_prereg.md` — FROZEN ALONE @ `b883c9b4` (prereg-first, git-provable). Phase-2 code @ `5cf9553c` (engine additions + keepers + driver with §210 deviations stated in the header, committed BEFORE the run's numbers existed). This doc reads ONLY from `research/2026-06-11_annihilation-evaporation-run_results.json` (ave-driver-script-honesty; run exit 0, 22 runs, 889 s wall).
**Engine:** `src/ave/core/annihilation_engine.py` (`AnnihilationEngine` ← `UnifiedGenesisEngine`; NO `step()` override — inherited physics byte-identical, keeper-pinned).
**Keepers:** `src/tests/test_annihilation_evaporation.py` — 6/6 green (BYTE-IDENTITY, K-DRIVE-EQUIV, K-HANDED, K-BURST, K-MASS, K-TRANSPORT); inherited v6 suite 10/10 green.

---

## 0. STATUS BLOCK — THE FROZEN-BIN VERDICT

> **MAIN bin: UNRESOLVED (wrong-regime artifact — the encounter never happens).** Per the frozen §7 ordering, F-TRANSLATE FAILS (the object moves **0.06** of the within-window-expected **0.62** cells; transport is structurally absent) and overlap-rupture is **never reached** in any approach arm — so per §1.5 every approach-arm null is a **wrong-regime ARTIFACT, not a falsification of annihilation**. ANNIHILATE did NOT survive; neither did it cleanly fail — **this architecture cannot pose the annihilation question dynamically.** Three mechanisms are NAMED (§7.1 below): transport-absent, release-channel-absent (the pre-run structural flag, empirically confirmed by C-static-overlap), handedness-dynamically-inert (the §2 ontology reading B).
> **What DID survive (floor-clean, field-level, consistency-class):** the §5 conservation-by-channel handedness ledger is EXACT — `L_total(RH+LH) = −1.4e-16 ≈ 0` (AM-allowed) vs `L_total(RH+RH) = −1.087 = 2L` (AM-forbidden); `H_bel(RH+LH) = 0.0` vs `H_bel(RH+RH) = −0.277 ≈ 2×` the v6 single-object `−0.138`. The opposite-handed pair IS the sign-reversed AM/charge ledger, exactly as inherited. And the v6 T1 converged dilatation mass is **column-independent** (DEV-1 re-measure: single object `E_V^cons = 12.86`, inside the v6 N-robust band 12.86–12.91).
> **NOT-ELECTRON stands; no claim is promoted; the condensation ontology's evaporation half remains OPEN (untested at this architecture).**

## 1. §210 DEVIATIONS — STATED BEFORE THE RUN (committed @ `5cf9553c`, pre-results)

- **DEV-1 (no per-object rotation column).** The v6 DRIVER also energized a GLOBAL rotation column (M=1.8, grid-center z-axis). The prereg §0.1 FROZEN recipe enumeration does not include it; the capability is global-axis-only (cannot be placed at c_A/c_B); a centered column would contaminate the load-bearing net-AM channel (the v6 GEOMETRIC false positive: `core_sense_u` 20.00 ≈ achiral 20.00). RE-BIN: the T1 build-validity gate re-measured at this config — **PASS** (drift 0.0071 < 0.05; per-object mass in the v6 band).
- **DEV-2 (additive per-object photon drive).** The inherited `seed_photon` ASSIGNS `w_prev` components (`crystal_engine.py:325-326`) — a second drive call clobbers photon A's group-velocity imprint. `drive_chiral_photon_at` accumulates additively; single-call value-identity keeper-pinned (K-DRIVE-EQUIV).
- **DEV-3 (C-static-overlap is PLACED).** No converged-object transplant capability exists or was frozen; the geometric control seeds the two objects co-located (superposed seed, placement A = 1.66) + both drives.
- **DEV-4/DEV-6 (fixed 3600-step encounter windows).** The lineage CFL (graft-v2 `S_min = 1e-4` ⇒ `c_eff_max = 100`) gives `dt = 0.001732`; closing 18 cells at `v_approach = 0.2` needs **n_close = 51,962 steps** (recorded per-run), AND the N=32 smoke showed ZERO centroid motion over 17k steps. All encounter windows FIXED at 3600 steps; never-met arms LABELLED wrong-regime per §1.5; F-TRANSLATE's "arrives" criterion re-binned to the within-window expected displacement; K3 stop-time {1200, 2400, 3600} read as encounter-series cut-points.
- **DEV-5 (threshold_mult in post).** The full un-decimated per-step released history (3601 frames) re-scanned at {2.0, 3.0, 5.0}× the calibrated floor.
- **Post-`5cf9553c`, pre-launch analysis-layer edits (honesty note).** Between the code commit and the run launch, three ANALYSIS-layer changes landed (committed with the results): un-decimated released history (DEV-5 exactness), build-phase strain in the regime witness, and the §7.1 never-met ordering in the classifier. The PHYSICS layer is unchanged — provable from the record: the run's build series and the F-BURST floor are bit-identical to the pre-launch pre-flight (`F_BURST = 2.0500621478340694e-35` both).

## 2. THE PRE-RUN STRUCTURAL FLAG (flag-don't-fix; recorded at `5cf9553c` before any number) — EMPIRICALLY CONFIRMED

Code-reading: the V/w/ω sectors and the ρ̄/u bulk sector are dynamically INDEPENDENT (GAP-C couplings default-OFF; `_bulk_rhs` reads only ρ̄,u; graft v2–v4 never reference ρ̄/u). The burst detector reads ONLY snap-machine ledgers; the snap fires ONLY on ρ̄ ≤ ρ̄_cav = −0.618 crossings; the converged object's latent store is V-sector. The only V→ρ̄ path (V→converter→w→transducer→u_adv→ρ̄) is OOMs below the cavitation floor.

**Empirical confirmation (the run):** deepest ρ̄ anywhere in any arm = **−6.7e-5** (C-same-handed, the transducer stirring) vs the −0.618 floor — **4 OOM short**; in MAIN `ρ̄_min = −6.6e-22` and in C-static-overlap `ρ̄ ≡ 0.0` exactly. `p_integral ≡ 0.0` at every K3 cut. **The evaporation/burst channel is structurally absent at this architecture**, exactly as flagged before the run.

## 3. FLOORS (ordered, evaluated FIRST — every value from the JSON `analysis.floors`)

| floor | known-null / reference | value | gate consequence |
|---|---|---|---|
| F0a (mass background) | empty box, 200 steps | **0.0** (exact) | "→ background" = a strict zero read; never approached |
| F-BURST | built static pair (per-run deepcopy, 200 steps) | **2.05e-35** (machine zero — the bulk channel is silent) | any genuine release would clear it; NONE did (0 bursts everywhere) |
| F-CLOSE | C-no-approach window, `H_total^cons` max positive excursion | **0.0000** | MAIN excursion **0.0000** ⇒ NO pump; ledger closes exactly (dissipative only) |
| F-RADIATE | C-no-approach net w-loss (free dispersion) | −0.0306 | MAIN net radiate +0.0111 — within the floor's scale ⇒ NO above-floor transverse remainder |
| **F-TRANSLATE** | C-translate single object, v_obj = 0.1, window 3600 | moved **0.0600** cells of **0.6235** expected; leak 1.41 % | **FAILS (arrived = false)** ⇒ per frozen §7.1 the two-body encounter verdict is INADMISSIBLE → UNRESOLVED |
| F0c | per-step reactance pairs (C+L states), both objects, whole window | complete = **true** (3600/3600 frames, finite) | lock-vs-unbind reads admissible |
| T1 gate (DEV-1 re-measure) | this config's own build series | drift **0.0071** < 0.05; per-object 12.55–12.86 | **PASS** — the objects under test are converged v6-class masses |

## 4. THE ARM MATRIX (frozen §6) — RESULTS

| arm | T1 | built E_V^cons | KE_app (η_KE) | bursts | strain_max (enc / incl-build) | ρ̄_min | final E_V^cons | x-peaks | frozen-§7 bin |
|---|---|---|---|---|---|---|---|---|---|
| **MAIN** (RH@c_A, LH@c_B, v=0.2) | PASS | 25.34 | 0.0747 (0.0015) | **0** | 0.382 / 0.830 | −6.6e-22 | 25.10 | 3 | **UNRESOLVED (wrong-regime: never-met)** |
| **C-same-handed** (RH, RH, v=0.2) | PASS | 25.33 | 0.0747 (0.0015) | **0** | 0.385 / 0.830 | −6.7e-5 | 25.09 | 3 | UNRESOLVED (wrong-regime: never-met) |
| **C-translate** (single RH, v=0.2) | PASS | 12.86 | 0.0175 (0.0006) | 0 | 0.392 / 0.830 | −6.7e-5 | 12.69 | 1 | **F-TRANSLATE FAIL** (moved 0.06/0.62 cells) — the transport finding, itself valuable |
| **C-no-approach** (RH, LH, static) | PASS | 25.34 | 0 | **0** | 0.384 / 0.830 | −6.6e-22 | 25.36 | 3 | the floors' known-null (F-BURST/F-CLOSE/F-RADIATE measured here) |
| **C-static-overlap** (RH+LH co-located) | n/a (probe control) | 105.63 | 0 | **0** | 0.660 / **1.661 ≥ 1** | **0.0 exact** | 104.64 | 1 | **MERGE-class; the geometric discriminator: dilatation rupture reached BY PLACEMENT → still NO burst, NO evaporation** |

Notes (all from JSON): MAIN per-object windowed masses exactly symmetric (12.6687/12.6687 built → 12.5499/12.5499 final). The known-null's classifier fall-through label ("BOUNCE-or-PASS-THROUGH") is cosmetic — it is a floor arm, not a verdict arm (flagged in §9). C-static-overlap's T1 gate fails (drift 8.3 %) as expected for a placement-superposed probe control; its admissible read is the BURST channel only.

## 5. THE MANDATED SWEEPS (§210 gate — ALL executed; verdict knob-invariant)

| knob | grid (run) | result | CLIP telltale check |
|---|---|---|---|
| `v_approach` | {0.05*, 0.1, 0.2, 0.4, 0.8} (*fixed 1200 window = regime bracket) | 0 bursts at every v; centroid motion ≡ 0.0; η_KE 0.0002→0.0149 (all ≪ 1, D3 honored) | no verdict tracks v — the no-encounter null is v-invariant |
| `b` | {0, 3, 6, 10} cells | 0 bursts; identical no-encounter nulls | b-invariant |
| `N` | {40, 48, 56} | 0 bursts; per-object mass 12.56/12.67/12.86 (v6-band) | N-invariant (K2 clean) |
| `chi_exch` | {0, 0.005, 0.02, 0.08} | 0 bursts at every χ̃ incl. χ̃=0 | criterion 7.e selectivity never invoked (no positive exists) |
| `frac` | {0.30, 0.60, 0.85, 0.95} | placement strain 0.293/0.586/0.830/0.928 — **all converged objects relax to A≈0.13–0.44**; 0 bursts | the D1 bracket executed; see §7.2 (D1 holds at PLACEMENT only) |
| `meissner` | {0, 0.05, 0.10} | bit-identical nulls (snap never fires) | invariant |
| `threshold_mult` | {2.0, 3.0, 5.0} (post, full history) | 0/0/0 bursts MAIN and C-same | threshold-invariant |
| K3 stop-time | enc cuts {1200, 2400, 3600} | E_V^cons 25.35/25.45/25.10; `p_integral` 0.0 at every cut | no stop-time dependence |

## 6. CONSERVATION-BY-CHANNEL LEDGER (§5) — every number a FIELD quantity (§9 gross-vs-field)

| channel | observable | result |
|---|---|---|
| Longitudinal/bulk | `Δ total_burst_energy` MAIN − C-same | **0.0 − 0.0 = 0.0** (no release; the channel is structurally absent, §2) |
| Transverse/EM | net w-loss MAIN − known-null | +0.0111 vs floor −0.0306 ⇒ no above-floor remainder |
| Rotational/AM | `L_total` field (bulk + ω-axial) | **MAIN (RH+LH): −1.39e-16 built → +5.09e-15 final (≈0 throughout — EXACT cancellation)**; C-same (RH+RH): **−1.087 built → −1.157 final (= 2L, conserved to 6 %)** |
| Charge (Beltrami) | `H_bel` | **MAIN: 0.0 built (exact cancellation)**; C-same: **−0.277 ≈ 2 × v6 single −0.138** (verify-before-cite: v6 JSON `Hbel = −0.1384`) |
| Energy closure | `H_total^cons` positive excursion | **0.0000 in MAIN and in the known-null** — energize-once-then-coast honored; no pump (ave-conserved-vs-pumped) |
| Approach KE | `KE_approach` (field delta of the conserved functional) | MAIN 0.0747, η_KE = 0.0015 ≪ 0.1 (D3 slow-approach discipline honored) |

**Handedness contrast in the DYNAMICS (the §2 discriminator):** final-mass contrast MAIN − C-same = **+0.0094 of 25.1 (4e-4 relative)**; strain contrast **−0.0025**. The two configurations' dilatation dynamics are **handedness-BLIND to ≲0.04 %** while their conserved ledgers differ EXACTLY (0 vs 2L; 0 vs −0.277).

## 7. THE FROZEN BINS — VERDICT (ordered, Rule 11)

**Gate 1 (floors): F-TRANSLATE FAILS** ⇒ the two-body encounter verdict is INADMISSIBLE → **UNRESOLVED**. **Regime witness:** overlap-rupture never reached in ANY approach arm (max encounter strain 0.391 < 1.0; cavitation 4 OOM short) ⇒ per §1.5 every approach-arm no-burst null is a **wrong-regime ARTIFACT — labelled, NOT a falsification of annihilation**.
**Gate 2 (knob-tracking):** no positive exists; the null is invariant across every §8 knob (no CLIP).
**Gate 3 (verdict bins):** not reached for MAIN (gated at 1). C-static-overlap (the only arm that ever attains overlap) bins **MERGE-class**: one blob, residual mass 104.6 persists ≫ F0a = 0, no burst, no evaporation — at a configuration where the dilatation rupture witness WAS reached by placement (A = 1.66 ≥ 1).

### 7.1 The three NAMED mechanisms (Rule 11 honest closure — no debugging toward ANNIHILATE, no criterion drop)

1. **TRANSPORT-ABSENT.** The V-sector scalar wave equation (∂²V = c_eff²(V)∇²V) admits no subluminal rigid translation of a trapped blob; the §4.2 drift imprint puts real momentum into the field (KE_approach > 0, keeper-verified bookkeeping) but the trap does not convect — centroid motion 0.06/0.62 cells (C-translate), 0.000 at every v in the sweep. The v6 "motion-lock" (D-PERM) lives in the `u_adv` advective channel, which is dynamically decoupled from V. **A v6-class dilatation mass has no transport degree of freedom at this architecture.**
2. **RELEASE-CHANNEL-ABSENT (the §2/§0.2 reverse-reaction channel does not exist in this engine).** The latent store is V-sector; the burst/flash detector reads the ρ̄ snap ledger; NO V→ρ̄ coupling exists (GAP-C, default-OFF, never wired). C-static-overlap is the clean demonstration: dilatation overlap-rupture BY PLACEMENT → ρ̄ stayed identically 0.0 → no snap, no latent tally, no burst. The genesis-direction transduction (transverse→longitudinal-stored) ran through the ρ̄ snap machine; the REVERSE (V-stored→released) has no path back.
3. **HANDEDNESS-DYNAMICALLY-INERT (§2 ontology answer = reading B, with a precise refinement).** The opposite-handed pair is a REAL sign-reversed conserved ledger (L_total and H_bel cancel EXACTLY — bookkeeping-real, consistency-class) but the handedness does NOT couple back into the dilatation dynamics (contrast ≲ 4e-4). Two v6 objects are scalar dilatation blobs decorated by a dynamically-inert charge ledger — at the merge/encounter level, opposite-handed ≡ same-handed, exactly the v6-DEMOTION-anticipated reading.

**A44 disposition:** an engine coupling-family limit (two missing couplings: V-transport, V↔ρ̄ release), NOT a missing axiom. No Ax-5 candidate is drafted. A v7-class architecture (a transport-capable carrier + a wired V↔ρ̄ release channel) is a NEW hypothesis requiring its own prereg (Rule 12: this slot is not refilled here).

### 7.2 Step-3.5 dimensional predictions (§10) — scored honestly

- **D1 (`R_rupt = 2·frac`):** holds at PLACEMENT (frac sweep placement strains 0.293/0.586/0.830/0.928 ≈ 0.977·frac; co-located placement 1.66 ≈ 2×0.83 ✓). **New empirical regime fact: the CONVERGED object relaxes to peak strain ≈ 0.38–0.44 (≈ 0.45·frac at 0.85)** — so two CONVERGED objects superposing would reach only ≈ 0.78 < 1: rupture-by-superposition of converged masses is NOT reachable at frac = 0.85, only placement-fresh seeds reach it. D1's leading-order estimate was placement-correct but converged-wrong; recorded, not papered over.
- **D2 (M_app):** all approach arms ran at M_app ≤ 0.8 with the headline at 0.2; the dynamic-shock route was never reached (no transport ⇒ no closing flow at all).
- **D3 (η_KE ≪ 1):** honored at every point (max 0.0149); the burst-provenance question never arose (no burst).

## 8. THE §2 ONTOLOGY ANSWER

> *Is the "opposite handedness" of two v6 objects a REAL charge-conjugate, or only the tiny lock-limited remainder decorating two scalar dilatation blobs?*

**Answer (empirical, this run): reading B, refined.** The handedness is a REAL and EXACT conserved-ledger conjugate (L_total and H_bel cancel to machine precision for RH+LH; double for RH+RH — the cleanest conservation-by-channel demonstration in the genesis arc) — but it is **dynamically inert**: it opens no annihilation channel, alters no dilatation dynamics above 4e-4 relative. The §2 anticipated consequence follows: at the dilatation level opposite-handed ≡ same-handed, and the run is uninformative for annihilation BY CONSTRUCTION — which is exactly why the verdict is UNRESOLVED (wrong-regime/missing-channel), not NEGATIVE. The §2 gate's wrong-noun risk materialized in the apparatus, and the ordered bins caught it honestly.

## 9. PANEL DISPOSITION (adversarial lenses, post-run; the record's demotions)

1. **PREREG-FIRST lens — clean with one flagged nuance.** Chain: prereg ALONE `b883c9b4` → code + stated deviations `5cf9553c` → run → results. NUANCE (disclosed §1): three analysis-layer edits (classifier ordering, witness completeness, history un-decimation) landed after `5cf9553c` but before launch; physics-layer bit-identity is provable from the record. No demotion; transparency note stands.
2. **ONTOLOGY-GATE lens — flagged for Grant.** Prereg §2 gated the run on Grant's answer; the orchestrator dispatch collapsed the gate (the §2 flag-don't-fix anticipated "run it and see" — both readings were frozen as non-failing bins). The run's reading-B outcome is exactly the §2-anticipated uninformative-for-annihilation case. **Surfaced, not silently resolved: Grant should ratify the gate-collapse retroactively in PR review.**
3. **GROSS-VS-FIELD lens — clean.** Every §6 ledger number is a field functional or a net MAIN−control contrast; the per-step accumulators (`L_transferred`, released tallies) appear only as channel bookkeeping, never as headlines.
4. **OVER-CLAIM lens — two demotions applied.** (a) "The conservation ledger works" is **consistency-class** (the transducer/buckle wiring conserves by construction; the run demonstrates the two-object SIGN ledger composes exactly — a non-trivial but consistency-class check), NOT an emergence result — headline tagged accordingly. (b) "Transport structurally absent" is demonstrated **for the §4.2 V_prev-imprint mechanism at v ≤ 0.8, N ≤ 56**; a different transport rendering (e.g., advected-frame or boosted-soliton ansatz) was not frozen and was not tested — the claim is scoped to this architecture's available mechanism.
5. **CLASSIFIER lens — one cosmetic flag.** The known-null arm's fall-through label ("BOUNCE-or-PASS-THROUGH") is meaningless for a no-approach floor arm; binned here as floor-arm, label ignored. No number affected.
6. **WRONG-REGIME lens — clean.** The §1.5 discipline is applied in BOTH directions: the nulls are not sold as falsification, and the structural findings are not sold as annihilation-negative evidence.

**Panel outcome: the record survives with the §0 verdict intact; demotions 4a/4b applied in place; flags 1/2/5 disclosed.**

## 10. CORPUS STATE

- **OPEN.** The annihilation/evaporation question remains untested-at-architecture; the condensation ontology's evaporation half is neither demonstrated nor falsified. The bidirectionality claim (genesis ⇄ evaporation) is **NOT** demonstrated — the genesis half stands as previously recorded (hypothesis-class), the evaporation half is blocked by two named missing couplings.
- **NOT-ELECTRON stands** (v5/v6 panels, un-reopened). No claim promoted; no walk-back triggered (no prior corpus claim asserted this engine could annihilate).
- **Valuable standalone findings:** (i) the v6 converged dilatation mass is rotation-column-independent (12.86 vs the v6 12.86–12.91 band); (ii) a v6-class mass has no V-sector transport DOF; (iii) converged-vs-placement strain relaxation (0.85 → 0.38) re-scopes D1-style rupture estimates for ANY future two-body design; (iv) the exact two-object sign-ledger composition.
- **Next (requires its own prereg; NOT started here, Rule 12):** a v7-class two-body architecture needs (a) a transport-capable carrier (the u_adv advective sector hosts motion — D-PERM — but carries no V-mass) and (b) a wired V↔ρ̄ release coupling (the GAP-C surface, adjudication-gated).

---

*Disciplines fired in the run phase, retroactive pass: ave-apparatus-floor-attribution v1.1 (ordered floors first, per-run F-BURST recalibration, every knob swept or deviation stated pre-run); ave-driver-script-honesty (this doc reads only the JSON); ave-regime-phase-state-check (never-met = wrong-regime artifact, both directions); ave-conserved-vs-pumped (energize-once verified: H excursion 0.0000); consistency-vs-emergence (ledger results tagged consistency-class); ave-evidence-framing-discipline (panel demotions 4a/4b); verify-before-cite (v6 anchors re-pulled from the v6 JSON this session); flag-don't-fix (ontology-gate collapse + analysis-layer-edit nuance + classifier cosmetic flag all surfaced).*
