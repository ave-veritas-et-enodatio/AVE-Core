# RESULT — Genesis-v6 PHASE 3: the GENESIS-RUN MATRIX under the LIVE chiral-boundary transducer

**Date:** 2026-06-10
**Prereg (FROZEN, committed ALONE @ `8b7aa40a`):** `research/2026-06-10_genesis-v6-transducer_prereg.md` §7
**Driver:** `src/scripts/vol_1_foundations/genesis_v6_transducer_run.py` (parallel via `genesis_parallel_runner`; spawn-safe, `serial==parallel` bit-identical — validated; seed `20260610`)
**Raw numbers:** `research/2026-06-10_genesis-v6-transducer-run_results.json` (every number below read FROM it — ave-driver-script-honesty)
**Engine:** `src/ave/core/unified_genesis_engine.py` — D9 transducer + the PHASE-3 ω-recipient (`omega_recipient_frac`); v5/smoke path byte-identical by default (`src/tests/test_unified_transducer_v6.py` 10/10 + the inherited suite green)
**Figures:** `research/figures/fig_v6_{T1_mass,omega_chiral,winding_question,nu_art_dperm}.png`

---

## 0. THE QUESTION OF THE NIGHT — answered from the numbers

> *With the transducer LIVE, does the photon's helicity finally become WINDING — `w_pol ≠ 0`, above the extractor floor, helicity-odd, absent in transducer-OFF?*

**Helicity became CHARGE/AM — NOT quantized WINDING.** The transducer couples photon helicity into the bulk ω carrier as a **perfectly helicity-odd, depleting, passive AM/charge** channel (`L_transferred_omega = ∓0.539`, odd-fraction **1.000**, ∝χ̃, transducer-OFF structural-null, `E_absorbed ≥ 0`; `H_bel = ∓0.138`, achiral true-null `1.2e-19`) — it BREAKS the v5 four-arms-byte-identical inertness. **But `w_pol` does NOT become a quantized winding:** it is **0 across the ENTIRE χ̃ ladder {0, 9e-4, 0.005, 0.02, 0.08} AND the entire ω-recipient ladder {0, 0.5, 1.0}**; the lone `w_pol=1` at the MAIN 3200-build sits AT the reliability floor (rel **0.109** vs the 0.1 gate), does NOT track the coupling, and **appears in the achiral arm too** — it is a floor-grazing read, not a coupling-driven `(2,3)`. The poloidal **"3" never forms.**

## 1. SPEC-SHEET VERDICT — **PARTIAL** (T1 passes; the winder/spin/twin localize → the NAMED RESIDUAL)

Per the FROZEN §7.5 bins. **T1 (primary) PASSES; ≥4 of T2–T6 do NOT pass at their floors; the winding localizes to `w_pol≡0` DESPITE the live transducer → PARTIAL.** This is the prereg's explicitly-anticipated bin (A44: an engine coupling-family gap, NOT a missing axiom; NOT auto-pivoted). NOT-ELECTRON (the v5 panel) was NOT reopened and is NOT overturned — the electron claim stays closed; v6 built the missing primitive and answered the new question.

| test | floor-check (first) | result | bin |
|---|---|---|---|
| **T1 mass (primary)** | `H_total^cons`/`E_V^cons` late-drift < 5% AND `E_V` bounded < 10×F-EV (no deflagration) | `E_V^cons` **11.70→12.91** (drift **0.86 %**), `H_total^cons` drift **0.83 %** → **CONVERGED**; N-robust (12.86–12.88), stop-time-robust (K3: 12.87–13.00), `E_V` bounded at every meissner | **PASS** (emergence-class: a converged dilatation mass) |
| **T2 charge** | F0b `r≥3` + Park-along-contours; reliability > 0.1 | `(w_tor,w_pol)=(1,1)`, `w_pol_rel=0.109` (floor-grazing); `is_2_3=False`; `w_pol≡0` across all χ̃ and all ω-frac; w_pol=1 also in achiral | **FAIL → NAMED RESIDUAL** |
| **T3 spin** | F0c + η-invariance of locked `L_ω` | `spin_L_omega` tracks `lock_eta`: **5.634 (η=0) → 0.0099 (η=0.12)**, a 570× swing | **CLIP** (the v5 T3 CLIP reproduced) |
| **T4 kick** | F0a + re-verify T1/T3 post-perturb | RE-VERIFIED (finite, bounded, decreasing) — but the 0.02 noise injection dominates the kicked energies; weak, moot given T2 | weak PASS (caveat) |
| **T5 twin (sharpened)** | C-achiral known-null ≈0 | global handedness **BALANCED** (born-in-pairs); helicity-odd signature is **SELECTIVE in the AM/charge ledger** (`H_bel` ∓0.138, achiral 1.2e-19) but the spatial vorticity twin is **GEOMETRIC** (`u` core_sense = 20.00 column-dominated, RH≈achiral; ω-vorticity core_sense not helicity-odd) | **MIXED** (chiral in charge; geometric in vorticity) |
| **T6 de Broglie** | weight-bearing only if a real winder exists | `λ` flat (24.0 at every p), slope ≈0 → NOT-INVERSE-P | FAIL (moot — no winder) |

## 2. THE TRANSDUCER IN THE FULL ASSEMBLY — it DID convert helicity to a bulk coupling (the v6 half-win)

The D9 transducer + ω-recipient is LIVE and behaves EXACTLY as designed at the channel level — it is the **depleting boundary coupling the BEMF smoke demanded**, now firing inside the full seed+snap+buckle+lock assembly:

- **Helicity-odd, 1:1, passive (the AM/charge channel):** `L_transferred_omega` = **−0.5388 (RH) / +0.5388 (LH)**, odd-fraction **1.000**, exact sign-reversal; the combined AM ledger closes 1:1; `passive_no_pump=True` across the whole χ̃ sweep. `H_bel` = **−0.1384 (RH) / +0.1384 (LH)**, achiral = **+1.2e-19** (true null from the field).
- **D9-isolated (MAIN − C-transducer-OFF, same RH):** `ΔL_transferred_omega` above **100×F-EXCHANGE** (F-EXCHANGE = 5.3e-18, a structural zero); `ΔL_omega,axial` = −3.6e-5; `ΔH_bel` = −0.0198. The transducer's own contribution is unambiguously above floor.
- **∝χ̃ control scaling (NOT verdict-tracking):** `|L_transferred_omega|` scales monotonically with χ̃ (0→0.157→0.351→0.499→0.626) and with `omega_recipient_frac` (0→0.468→0.935) — the expected control-parameter scaling; the **sign/oddness/null are INVARIANT** across χ̃ and `wall_width`. The verdict does not track the magnitude (§210-clean).

**What it did NOT do:** make the ω carrier QUANTIZE. Depositing helicity-odd AM into ω (even 100 % of it, `omega_frac=1.0`) leaves `w_pol=0`. **Helicity → charge/AM is solved; helicity → the poloidal `(2,3)` winding is the residual.** Refined A44 statement: the gap is no longer "no coupling" (v5's inert bulk) — it is **"a helicity-odd AM/charge coupling that does not self-organize the winding quantization."** The transducer torques the angular pair; it does not, by itself, knot it.

## 3. THE MOTION-LOCK RE-CHECK (D-PERM) — MOTION-LOCKED, PHYSICS (re-confirmed under the live transducer)

- **P1 `L_bulk` persistence:** MAIN ratio **0.970**, C-LH **0.970**, **C-no-snap 0.995** (persists BETTER without the snap) — the lock is the **circulation, not the snap**.
- **ν_art-INVARIANT (the D8 attribution):** across the 50× span {1e-4…5e-3}, `L_ratio` = **0.9998 → 0.9996** and the centrifugal `deficit = −0.0365` is **invariant to 4 sig-figs** — the motion-lock does NOT track viscosity ⇒ **PHYSICS**, not apparatus (v5's ν_art-invariant deficit −0.0516 re-confirmed at this config).
- **Snap-channel = CLIP (re-confirmed under the live transducer):** the `Δ_heal × payback` grid — P2 pocket retain = **1.0 ONLY at payback=0** (un-snap disabled); **0.0 for every payback>0** regardless of Δ_heal; `pocket_built` tracks the knobs (744→96). The snap does not lock the void; the transducer is orthogonal to it (JOB-3 CLIP holds).

## 4. THE CHIRAL TWIN (sharpened T5) — SELECTIVE in the charge channel, GEOMETRIC in the vorticity channel

The sharpened-T5 probe-capability discipline paid off live: **the v5 geometric false positive is demonstrated, not inherited.** The `u_adv` inner-disk circulation (`core_sense_u`) reads **20.00 for MAIN AND 20.00 for C-achiral** — byte-near-identical (the energized rotation column swamps the transducer's ~0.3 u-deposit) ⇒ a u-channel "twin" would be the **GEOMETRIC v5 false positive** (the column, not the chirality). The genuine helicity-odd twin lives in the **AM/charge ledger** (`H_bel`, `L_transferred_omega`: present in MAIN & C-LH, sign-flipped, true-null in C-achiral) — **SELECTIVE there**. The ω-vorticity `core_sense` is NOT helicity-odd (RH≈LH, both 8.7e-9) ⇒ no spatial counter-rotating partner. **Bin: the chiral twin is real in charge, geometric in vorticity** — there is no emergent counter-rotating spatial twin, only the charge-ledger sign-flip.

## 5. THE BIRTH FLASH (D6) — rides again, unchanged

At the K3 stop-time = 4000 point the snap fires (onset **step 3396**, pocket **1208**): the burst detector records **561 bursts, total energy 7.12**, individual magnitudes ~4e-3–6e-3 ≈ **40–70× the F-BURST gate** (9.2e-5). The birth flash is intact and well above floor. **§210 DEVIATION (stated):** at N=48 the snap onset (3396) exceeds the FROZEN `n_build=3200` (onset TRACKS N — the K2 CLIP: 2849→3396→>3600 for N=40→48→56), so the flash is captured at the mandated K3=4000 stop-point; the spec-sheet stays at the frozen 3200 (no goalpost move — Rule 11).

## 6. THE END-TO-END LEDGER (post-D11 closure) — closes, dissipative, no pump

`H_total^cons`: build-start **29 203** → built **24 612** (decreasing — the correct dissipative sign; the snap-reflector + open PML are one-way sinks). **Pump pre-gate (D12, drive-off): max positive excursion 0.0000 % ≤ F-CLOSE (0.0 %) — PASS.** The v5 +283 % H pump (vent→breather + wrong-functional + double-count) stays fixed at N=48; the genesis arm ran without an honest block.

## 7. FAIL-FAST + FLOORS (ORDERED BINS — evaluated FIRST)

- **D12(i) transducer-alive:** `max|u_RH−u_LH|@200 = 2.0e-3`, `max|ω_RH−ω_LH|@200 = 7.0e-3` > 0 ⇒ ALIVE (matrix ran).
- **D12(ii) achiral:** the TRANSDUCER's achiral deposit is the structural null (`L_transferred_omega ≡ 0`, keeper-confirmed); the reported `achiral_null=False` is the **inherited BUCKLE** sourcing ω for the achiral (linear-pol) drive — NOT a transducer pump (see §8 flag). The transducer's own achiral channel is exactly zero.
- **Floors (recalibrated at the Run config):** F-CLOSE = 0.0 (no positive excursion), F-EV = 12.05, F-BURST = 3.07e-5, F-EXCHANGE = 5.3e-18 (structural), F-PROBE **separates ±h** (S_rh −2.994 / S_lh +2.994 / S_ac 0.0 — the m-even keeper). F0e `L_bulk` drift −0.05 %.

## 8. FLAGS (flag-don't-fix — surfaced, NOT silently fixed; the auditor lands any manual entry)

1. **CONTAMINATION FLAG (§7.3, the load-bearing one):** **C-transducer-OFF is NOT handedness-null in the ω/charge channel** — the inherited 3-way buckle (director = the photon shear `w`, which carries the helicity) couples helicity→ω on its own (`H_bel_OFF(RH) = −0.119 ≠ 0`). So the clean v6 contrast is **MAIN − C-transducer-OFF at the SAME handedness** (which isolates the D9 increment, §2), NOT RH-vs-LH (which mixes buckle + transducer). v5's "four arms byte-identical" was specifically the **u_adv/L_bulk** channel (the buckle does not touch `u_adv`); the ω-charge channel was helicity-dependent via the buckle already — but produced `w_pol=0` (verify-before-cite: v5 spec-sheet `T2 w_pol=0` confirmed). The transducer adds a SECOND, ledger-clean helicity→ω path; neither path quantizes the winding. **(Caveat, stated:** the C-transducer-OFF-LH byte-identity probe ran at `n_build=600` vs OFF-RH at 3200 — build-mismatched; the qualitative buckle-helicity-coupling finding is robust by construction, the magnitude comparison is not matched.)
2. **Fork-A `τ_zx` is NOT WIRED:** `tau_zx_arm` is an inert flag (set, never entering any force/EOM) — C-τzx-on and C-τzx-off are **byte-identical by construction** (`H_bel` identical to 1e-14), NOT an empirical null. The literal τ_zx radiation-reaction feedback is unimplemented in the unified engine; testing it needs its OWN prereg (Rule 12), NOT a silent in-engine addition here.
3. **The NEW knob (ave-apparatus-floor-attribution v1.1):** the ω-recipient introduced `omega_recipient_frac` — inventoried and SWEPT {0, 0.5, 1.0} (a superset of the §7.6 mandated list; the §210 gate served). `w_pol≡0` across it ⇒ the named residual is robust to the ω-wiring strength up to 100 %.

## 9. CORPUS STATE + DISCIPLINE

- **OPEN → PARTIAL recorded.** NOT-ELECTRON (the v5 panel) STANDS — the electron claim was not reopened and is not overturned. The v6 advance is real and bounded: (a) **T1 mass now CONVERGES** (the D11 pump + D10 deflagration fixes converted v5's STILL-RISING `E_V 11.7→50 339` detonation into a converged ~12.9 mass — verify-before-cite: v5 `T1 STILL-RISING`, `E_V_last 50339` confirmed); (b) the **transducer broke the v5 inert-bulk byte-identity** with a helicity-odd, depleting, passive AM/charge coupling; (c) **D-PERM = MOTION-LOCKED** re-confirmed (ν_art-invariant). The residual is sharpened: **helicity→charge/AM solved; helicity→`(2,3)` winding-quantization NOT** (A44 engine coupling-family gap — NOT a missing axiom, NOT auto-pivoted to an Ax-5 draft).
- **Rule 11:** the bins were frozen pre-run; the verdict is written from the numbers; no criterion was dropped to convert the negative; the `w_pol=1` floor-grazer is binned as the apparatus floor read (does not track the coupling, present in achiral), not promoted.
- **Rule 12:** the v5 SNAP-LOCKED 🔴 demotion stands (snap-channel CLIP re-confirmed); no slot refilled. A future helicity→winding-quantization mechanism is a NEW hypothesis with its own prereg + verification chain.
- **The auditor lands any manual/manuscript entry; this result SURFACES the empirical finding only.**

---

## 10. FINAL-VERDICT ADDENDUM (2026-06-10, post-adversarial-panel) — DEMOTED-PARTIAL; §§0–9 PRESERVED UNCHANGED (KEEP-BOTH)

**Panel disposition (two lenses):** SPEC-SHEET+LEDGER lens — **refuted=false** (prereg-first git-provable `8b7aa40a`→`7b724834`; T1 ledger + convergence verified; ordered bins honest; the T5 geometric false-positive correctly excluded; the PARTIAL bin survives). TRANSDUCER-ATTRIBUTION lens — **refuted=true**: the §0/§2 HEADLINE over-credits the transducer in three grep-specific ways. Every demotion number below was independently re-verified against `2026-06-10_genesis-v6-transducer-run_results.json` in the final-verdict session (verify-before-cite). **The frozen §7.5 PARTIAL bin HOLDS; the content of the positive inside it is DEMOTED as follows.**

**DEMOTION 1 — the headline ∓0.539 is the by-construction ACCUMULATOR, ~4 OOM above the net field effect.** `L_transferred_omega = ∓0.5388` is the GROSS per-step deposit tally; the net field ω-axial AM the transducer actually adds is **`ΔL_ω(MAIN−OFF) = −3.605e-5`**. The lock (`_lock_relax`) drains essentially all of the deposit because the transducer deposits a **RIGID azimuthal rotation** (`unified_genesis_engine.py:513-514`) — exactly the mode the lock removes. The 1:1 AM ledger and the accumulator's odd-fraction 1.000 are bookkeeping identities, not field measurements. The genuine field effect IS real and survives attribution: helicity-odd from arm data (`L_ω,axial = −3.605e-5 (RH) / +3.605e-5 (LH)`, exact), absent in OFF (~1e-16), ~7e12× above the structural F-EXCHANGE floor, boundary-local (CP10 grep-verified: Gaussian shell in A, post-substep boundary op, no bulk EOM term), passive (`E_absorbed ≥ 0` at every χ̃). But it is **TINY and LOCK-LIMITED** — §2's lead number is restated to the field value.

**DEMOTION 2 — the `H_bel` "charge" half of "helicity→charge/AM" is BUCKLE-attributable; the attribution is STRUCK.** Decisive: `Hbel` is **INVARIANT to 6 sig-figs across `omega_recipient_frac` {0, 0.5, 1.0}** (−0.0251341 / −0.0251341 / −0.0251341) while the transducer's field deposit scales −6.7e-16 → −9.1e-4 → −1.8e-3 — routing 0 % vs 100 % of the extracted AM into ω changes the Beltrami charge by exactly nothing. Corroborated: `Hbel_OFF(RH) = −0.1186` is **86 %** of MAIN's −0.1384 (the inherited buckle, director = photon `w`, carries the helicity-odd charge — §8 flag 1 was the right flag but the headline kept the credit), and in the χ̃ sweep increasing χ̃ **REDUCES** |Hbel| (−0.0741 at χ̃=0 → −0.0382 at χ̃=0.08) — opposite-signed to the MAIN−OFF marginal (−0.0198), config-inconsistent. **Restated: the helicity-odd charge is the BUCKLE's (pre-existing in v5); the transducer adds a second, ledger-clean helicity→ω path that does not carry the charge attribution.**

**DEMOTION 3 — "∝χ̃" SOFTENED.** The net field ω-AM is **χ̃-FLAT** ({−4.8e-4, −5.5e-4, −4.7e-4, −3.6e-4} across the 89× χ̃ span, slightly decreasing) — **lock-limited, not coupling-limited**; the accumulator's curve (0→0.157→0.351→0.498→0.626) is monotone-SATURATING, not proportional. The verdict-critical invariances (sign, oddness, structural/true nulls) hold at every swept point, so §210 is not breached — but the prereg §6.6 L5 "∝χ̃" wording is withdrawn → **"monotone/saturating; sign-oddness-null invariant."**

**WHAT SURVIVES THE PANEL UNCHANGED:** T1 converged dilatation mass (E_V^cons ≈ 12.9, drift 0.86 %, N- and stop-time-robust — attributable to the D11 pump-fix + D10 deflagration hygiene, NOT the transducer); D-PERM = **MOTION-LOCKED PHYSICS** (ν_art-invariant over 50×, deficit −0.0365 to 4 sig-figs, persists better WITHOUT the snap); the snap-channel **CLIP** (retain=1.0 only at payback=0 — the v5 SNAP-LOCKED demotion confirmed, not overturned); the end-to-end ledger (dissipative, drive-off excursion 0.0000 %, no pump); the birth flash (561 bursts, 40–70× F-BURST); transducer boundary-locality + passivity; and the night's answer — **`w_pol ≡ 0` at every swept point: helicity did NOT become winding.** NOT-ELECTRON stands; the electron claim stays closed.

**FINAL BIN: PARTIAL (the frozen bin holds) — content demoted.** The transducer verdict is restated from "helicity→charge/AM solved" to: **a LIVE, passive, helicity-odd, depleting CHIRAL BOUNDARY COUPLING whose net field deposit (∓3.6e-5, rigid-azimuthal) is drained by the lock; the charge channel is the buckle's; the winding never forms.** The six-architecture question is answered **NO at this architecture**: the chiral wall converts helicity into exactly the rigid-rotation mode the lock is built to remove, and into nothing else.

**STRUCTURAL-BLOCK HYPOTHESIS (panel-surfaced, NOT adjudicated — a NEW v7 prereg question, Rule 12, no slot refilled):** the deposit geometry is rigid-azimuthal and `_lock_relax` removes precisely the rigid-rotation mode while preserving the local LC quadrature where the poloidal `(2,3)` lives — helicity→winding may be **structurally blocked by DEPOSIT GEOMETRY (rigid mode → lock sink)**, not by a missing coupling family. The v7 discriminator: a transducer depositing into the LC quadrature (a poloidal-projecting `δπ_ω`), with its own frozen prereg + verification chain.

**INDEPENDENT RE-EXECUTION (closes panel residual-risk #1):** in the final-verdict session, `make verify` was re-run live → **PASS** (ALL PHYSICS PROTOCOLS PASSED; defense-context clean, 957 files; predictions-manifest 36 entries pass) and the full unified-engine keeper family was re-run live → **40/40 green** (7 files incl. `test_unified_transducer_v6.py`; the earlier 24/36 counts were phase-subsets — `test_unified_drive.py` adds 5). Figure check: `fig_v6_omega_chiral.png` plots the FIELD `L_ω,axial`, not the accumulator — no figure correction needed.

**CARRIED FOLLOW-UPS (each needs its own prereg or a build-matched re-run; none block this record):** (1) build-matched C-transducer-OFF-LH (3200 vs 3200) to characterize the buckle's own helicity-oddness cleanly; (2) the ~13× MAIN-vs-χ̃-sweep net-field-ω discrepancy (−3.6e-5 vs ~−4.7e-4 at nominally equal χ̃) — config/build sensitivity uncharacterized; (3) Fork-A `τ_zx` wiring (inert flag) — own prereg; (4) the v7 LC-quadrature-deposit discriminator (above).
